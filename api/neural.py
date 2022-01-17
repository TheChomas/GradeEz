from sentence_transformers import SentenceTransformer, InputExample, losses, util
from torch.utils.data import DataLoader

# Define the model. Either from scratch of by loading a pre-trained model
# model = SentenceTransformer('all-mpnet-base-v2')
model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')
