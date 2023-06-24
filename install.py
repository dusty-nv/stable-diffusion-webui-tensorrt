import os

import launch


def install():
    print("installing extension 'stable-diffusion-webui-tensorrt'")
    
    if not launch.is_installed("tensorrt"):
        raise ModuleNotFoundError("could not find tensorrt python module")

    if not launch.is_installed("pycuda"):
        launch.run_pip(f'install pycuda', "pycuda")

    if not launch.is_installed("onnx"):
        launch.run_pip(f'install onnx', "onnx")

    print("done installing extension 'stable-diffusion-webui-tensorrt'")
    
install()
