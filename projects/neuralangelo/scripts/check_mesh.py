import os 
import numpy as np
import trimesh

processed_meshes = [
    'ClayBowl.ply',
    'Spade.ply',
    'Bamboo_New.ply',
    'WoodenFruitBoxNew.ply',
    'WoodenFruitBox.ply',
    'Helmet.ply',
    'ClayBear_prod.ply',
    'ClayBear.ply',
    'ConcreteBlock.ply',
    'Spade1.ply',
    'TissueBox.ply',
    'xc1jdd0_prod.ply',
    'xerlfdq_prod.ply',
    'xgvjegk_prod.ply', # skipping 5.8 GB 
]


def load_meshes(src_dir):
    for file in os.listdir(src_dir):
        if file.endswith(".ply"):
            if file in processed_meshes:
                continue
            path = os.path.join(src_dir, file)
            print(f"Loading mesh: {file}")
            mesh = trimesh.load_mesh(path)
            vertices = len(mesh.vertices)
            faces = len(mesh.faces)
            
            print(f"{file[:-4]} => Vertices: {vertices}, Faces: {faces}")
    
src_dir = "meshes/RC"
load_meshes(src_dir)