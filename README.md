# examination_model


# Directory structure
 Case when you build model on ML-Engine
  - main/main.py is required
  
 Case when you build model on local
   - model.pkl is required
   
# Training data location
always on BQ
 
# When this application get deployed on ML-Engine
|    |    |
| ---- | ---- |
|  When  |   get tagged  |
|  Tag pattern  |  `^v\d\.\d\.\d$`  |
|  Example  |  v1.0.0s |