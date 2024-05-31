from label_generator import LabelGenerator

def main():
    # Example usage
    shipment_info = {'address': '123 Example St'}
    mrw_generator = LabelGenerator('MRW')
    mbe_generator = LabelGenerator('MBE')
    
    print("MRW Label:")
    print(mrw_generator.generate_label(shipment_info))
    
    print("MBE Label:")
    print(mbe_generator.generate_label(shipment_info))

if __name__ == "__main__":
    main()