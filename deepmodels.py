from sdv.single_table import CTGANSynthesizer, TVAESynthesizer
from sdv.metadata import SingleTableMetadata

def generate_ctgan(data, epochs=200, batch_size=256):
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(data)
    model = CTGANSynthesizer(metadata, epochs=epochs, batch_size=batch_size)
    model.fit(data)
    return model.sample(len(data))

def generate_tvae(data, epochs=200, batch_size=256):
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(data)
    model = TVAESynthesizer(metadata, epochs=epochs, batch_size=batch_size)
    model.fit(data)
    return model.sample(len(data))
