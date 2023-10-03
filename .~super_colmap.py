import tqdm
from pathlib import Path
import numpy as np

from hloc import extract_features, match_features, reconstruction, visualization, pairs_from_exhaustive
from hloc.visualization import plot_images, read_image
from hloc.utils import viz_3d

tqdm.tqdm = tqdm.tqdm

images = Path('neuralangelo/datasets/sacre_coeur')
outputs = Path('neuralangelo/datasets/sacre_coeur')

sfm_pairs = outputs / 'pairs-sfm.txt'
loc_pairs = outputs / 'pairs-loc.txt'
sfm_dir = outputs / 'sparse'
features = outputs / 'features.h5'
matches = outputs / 'matches.h5'

feature_conf = extract_features.confs['superpoint_inloc']
matcher_conf = match_features.confs['superglue']

references = [p.relative_to(images).as_posix() for p in (images / 'mapping/mapping/').iterdir()]

extract_features.main(feature_conf, images, image_list=references, feature_path=features)
pairs_from_exhaustive.main(sfm_pairs, image_list=references)
match_features.main(matcher_conf, sfm_pairs, features=features, matches=matches)

model = reconstruction.main(sfm_dir, images, sfm_pairs, features, matches, image_list=references)
