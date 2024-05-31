from mrw_label_provider import MRWLabelProvider
from mbe_label_provider import MBELabelProvider

class LabelGenerator:
    """
    Handles label generation using the appropriate provider.
    """
    def __init__(self, provider_type):
        if provider_type == 'MRW':
            self.provider = MRWLabelProvider()
        elif provider_type == 'MBE':
            self.provider = MBELabelProvider()
        else:
            raise ValueError("Unsupported provider type")

    def generate_label(self, shipment_info):
        return self.provider.generate_label(shipment_info)