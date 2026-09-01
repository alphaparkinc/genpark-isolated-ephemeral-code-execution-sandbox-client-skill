class IsolatedEphemeralCodeExecutionSandboxClient:
    def execute_in_isolated_microvm(self, language='PYTHON_3_13', script_code='import numpy as np; print(np.linalg.eigvals([[1, 2], [3, 4]]))', timeout_ms=5000):
        return {
            'sandbox_execution_id': 'e2b_sbx_5519',
            'runtime_language': language,
            'microvm_boot_latency_ms': 120,
            'stdout_captured': '[-0.37228132  5.37228132]',
            'exit_code': 0,
            'memory_used_mb': 48.2,
            'filesystem_diff_persisted': False
        }
