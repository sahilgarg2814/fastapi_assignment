import numpy as np

def helper_normalise_and_scale_input_features(input_features, pipleine):
    """
    Scale input features using the provided scaler.
    
    Parameters:
        input_features (array-like): Input features to be scaled.
        scaler (MinMaxScaler): Scaler object for scaling the input features.
        
    Returns:
        array-like: Scaled input features.
    """
    input_features_array = np.array(input_features).reshape(1, -1)
    scaled_features = pipleine.transform(input_features_array)
    return scaled_features