from abc import ABC, abstractmethod

class LabelProvider(ABC):
    """
    Abstract base class for all label providers.
    """
    @abstractmethod
    def generate_label(self, shipment_info):
        """
        Generate a ZPL string based on the shipment information.
        """
        pass