import pyrender
import trimesh

import numpy as np

def hep_pyrender():

    trimesh.util.attach_to_log()

    eep_model = trimesh.load(
        'assets/detector/EEplus.obj'
    )

    eem_model = trimesh.load(
        'assets/detector/EEminus.obj'
    )
    
    eb_model = trimesh.load(
        'assets/detector/EB.obj'
    ) 

    beampipe_model = trimesh.load(
        'assets/detector/beampipe.obj'
    )
    
    EB = pyrender.Mesh.from_trimesh(eb_model)
    EEp = pyrender.Mesh.from_trimesh(eep_model)
    EEm = pyrender.Mesh.from_trimesh(eem_model)

    BP = pyrender.Mesh.from_trimesh(beampipe_model)
    
    scene = pyrender.Scene()

    light = pyrender.PointLight(
        color=[1.0, 1.0, 1.0],
        intensity=10.0
    )
    
    scene.add(EB)
    scene.add(EEp)
    scene.add(EEm)
    scene.add(BP)
    
    scene.add(light)
    
    pyrender.Viewer(scene)
    

if __name__ == '__main__':
    hep_pyrender()
