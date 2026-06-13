
# PYTHON CLASSES: FOUNDATIONS TO MLOPS & ML RELIABILITY


import logging
from abc import ABC, abstractmethod

# Configure a basic logger. In MLOps, we NEVER use print() for for critical info.
# We use logging to track what our objects are doing in production
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


# PART 1: THE ABSOLUTE FOUNDATION (Blueprint & Instance)

class BasicModel:
    """
    A class is a blueprint. It defines data (attribute) and behavior (methods)
    """
    def __init__(self, name):
        # 'self' refers to the specific object  being created.
        # We bind the 'name' argument to this specific object's memory.
        self.name = name

    def describe(self):
        # A method is a function that belongs to the class.
        # It can access the object's data via 'self'.
        logging.info(f"This is a basic model named: {self.name}")



# Instantiate (create) an object from the blueprint
model_a = BasicModel("LinearRegression")
model_a.describe()


# PART 2: ENCAPSULATION & VALIDATION (Critical for ML Reliability)

# In ML, bad data or invalid hyperparameters cause silent failures or crashes.
# We use the '@property' decorator to create "getter" and "setter" methods.
# This acts like a "bouncer", validating data before it is allowed into the object.

class MLConfig:
    def __init__(self, learning_rate):
        # We call the setter method here to ensure validation happens at creation
        self.learning_rate = learning_rate

    @property
    def learning_rate(self):
        # The 'getter': How we retrieve the value
        return self._learning_rate
    
    @learning_rate.setter
    def learning_rate(self, value):
        # The 'setter': How we assign the value, WITH VALIDATION
        if not (0.0 < value <= 1.0):
            raise ValueError("Learning rate must be between 0.0 (exclusive) and 1.0 (inclusive)")
        # We use '_learning_rate' (with an underscore) to indicate it's a 
        # private internal variable. Users should interact via the property.
        self._learning_rate = value


# Let's test the validation. 
safe_config = MLConfig(0.1)
logging.info(f"Safe config created with LR: {safe_config.learning_rate}")



# PART 3: ABSTRACT BASE CLASSES / INTERFACES (Critical for MLOps)
# In MLOps, you frequently swap models (e.g, swapping a Scikit-Learn model for a PyTorch model.)
# How do you guarantee the new model won't break the pipelin?
# You use an Abstract Base Class (ABC) to enforce a "contract".
# Any class that inherits from this ABC *MUST* implement the specified methods.

class PredictiveModel(ABC):
    """
    This is an interface. It cannot be instantiated directly.
    It forces any child class to implement 'predict' and 'get_version'.
    """

    @abstractmethod
    def predict(self, data):
        pass # Child classes must provide the actual code for this

    @abstractmethod
    def get_version(self):
        pass # Child classes must provide the actual code for this




class RandomForestModel(PredictiveModel):
    def __init__(self, n_trees):
        self.n_trees = n_trees

    # We MUST implement this, otherwise Python will throw a TypeError
    def predict(self, data):
        return f"Prediction with {self.n_trees} trees on data: {data}"
    
    def get_version(self):
        return "v1.2.0"
    

# This works because RandomForestModel fullfilled the contract
reliable_model = RandomForestModel(n_trees=100)
logging.info(reliable_model.predict("[1.5,2.3, 0.8]"))


# PART 4: COMPOSITION & DEPENDENCY INJECTION (Critical for ML Pipelines)

# Complex systems are built by combining simple objects. This is "Composition".
# Instead of a class creating its own dependencies, we "inject" them
# This makes code highly testable and modeular (a core MLOps principle)

class DataLoader:
    def __init__(self, data_source):
        self.data_source = data_source

    def load(self):
        logging.info(f"Loading data from {self.data_source}")
        return [1.0, 2.0, 3.0]
    
class Trainer:
    def __init__(self, model_object, data_loader_object):
        # We inject the dependencies. The Trainer doesn't care HOW the model
        # works or WHERE the data comes from, only that they have the right methods.
        self.model = model_object
        self.data_loader = data_loader_object

    def run_training(self):
        logging.info("Starting training pipeline...")

        # 1. Use the injected data loader
        data = self.data_loader.load()

        #2. Use the injected model (we know 'predict' exists)
        predictions = self.model.predict(data)
        
        logging.info(f"Training complete. Sample predictions: {predictions}")


# Create the independent objects first
my_loader = DataLoader("3://my-bucket/dataset.csv")
my_model = RandomForestModel(n_trees=50)

# Inject them into the Trainer. This is clean, modular, and reliable
my_trainer = Trainer(model_object=my_model, data_loader_object=my_loader)
my_trainer.run_training()



# PART 5: STATE MANAGEMENT & SERIALIZATION 

# In ML, you must be able to save an object;s state to a file (like JSON)
# and rebuild it later. We do this by creating 'to_dict' and 'from_dict' methods.

class ExperimentTracker:
    def __init__(self, experiment_name, learning_rate, accuracy):
        self.experiment_name = experiment_name
        self.learning_rate = learning_rate
        self.accuracy = accuracy

    def to_dict(self):
        """
        Serializes the object's state into a standard Python dictionary.
        This dictionary can easily be saved to a JSON file or a database.

        """
        return {
            "experiment_name": self.experiment_name,
            "learning_rate": self.learning_rate,
            "accuracy": self.accuracy
        }
    
    @classmethod
    def from_dict(cls, data_dict):
        """
        A 'classmethod' belongs to the class itself, not an instance.
        'cls' refers to the ExperimentTracker class.
        This acts as an alternative constructor to rebuild an object from dictionary.
        
        """
        return cls(
            experiment_name = data_dict["experiment_name"],
            learning_rate = data_dict["learning_rate"],
            accuracy = data_dict["accuracy"]
        )
    
# 1. Create an object
exp1 = ExperimentTracker("baseline_run", 0.01, 0.85)

# 2. Serialize it 
exp_dict = exp1.to_dict()
logging.info(f"Serialized state: {exp_dict}")

# Deserialize it
restored_exp = ExperimentTracker.from_dict(exp_dict)
logging.info(f"Restored experiment: {restored_exp.experiment_name} with accuracy {restored_exp.accuracy}")

