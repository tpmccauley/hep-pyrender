import pyrender
import trimesh

import numpy as np

def hep_pyrender():

    trimesh.util.attach_to_log()
    
    eb_model = trimesh.load(
        'assets/detector/EB.obj'
    ) 

    eep_model = trimesh.load(
        'assets/detector/EEplus.obj'
    )

    eem_model = trimesh.load(
        'assets/detector/EEminus.obj'
    )
    
    beampipe_model = trimesh.load(
        'assets/detector/beampipe.obj'
    )
    
    EB = pyrender.Mesh.from_trimesh(eb_model)
    EEp = pyrender.Mesh.from_trimesh(eep_model)
    EEm = pyrender.Mesh.from_trimesh(eem_model)
    BP = pyrender.Mesh.from_trimesh(beampipe_model)

    scene = pyrender.Scene(
        ambient_light=[0.03, 0.03, 0.03],
        bg_color=[0.0, 0.0, 0.0],
    ) 
    
    viewport_size=[1600,900]
    
    dl = pyrender.light.DirectionalLight(
        color=[1.0, 1.0, 1.0],
        intensity=5.0,
        name='directional light',
    )
    
    light_node1 = pyrender.Node(
        light=dl,
        translation=[1,1,1],
        scale=[10,10,10],
    )

    light_node2 = pyrender.Node(
        light=dl,
        translation=[-1,-1,-1],
        scale=[10,10,10],
    )
    
    scene.add_node(light_node1)
    scene.add_node(light_node2)
    
    scene.add(EB)
    scene.add(EEp)
    scene.add(EEm)
    scene.add(BP)

    pyrender.Viewer(
        scene,
        viewport_size=viewport_size,
    )
    
if __name__ == '__main__':
    hep_pyrender()
