
from transformers import AutoModelForMaskedLM, AutoTokenizer
import torch
from shark.shark_inference import SharkInference
from shark.shark_import
from shark.iree_utils.compile_utils import (
    get_iree_compiled_module,
    get_results,
    export_iree_module_to_vmfb,
    load_flatbuffer,
)
from shark.iree_utils._common import check_device_drivers, device_driver_info
from shark.parser import shark_args
import os
import sys


    def __init__(
        self,
        mlir_module: bytes = None,
        device: str = "none",
        mlir_dialect: str = "linalg",
        extra_args: list = [],
        compile_vmfb: bool = True,
    ):
        self.mlir_module = mlir_module
        self.device = shark_args.device if device == "none" else device
        self.mlir_dialect = mlir_dialect
        self.extra_args = extra_args

        if check_device_drivers(self.device):
            print(device_driver_info(self.device))
            sys.exit(1)

        if compile_vmfb == True:
            # Compile the module to get the .vmfb.
            (
                self.iree_compilation_module,
                self.iree_config,
            ) = get_iree_compiled_module(
                self.mlir_module,
                self.device,
                self.mlir_dialect,
                extra_args=self.extra_args,
            )

    def run(self, function_name, inputs: tuple, send_to_host=False):
        return get_results(
            self.iree_compilation_module,
            function_name,
            inputs,
            self.iree_config,
            self.mlir_dialect,
            send_to_host,
        )

    # Get all function names defined within the compiled module.
    def get_functions_in_module(self):
        return self.iree_compilation_module._vm_module.function_names
