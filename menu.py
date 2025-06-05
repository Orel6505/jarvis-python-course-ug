class Menu:
    def __init__(self):
        # dict: key=int option num, value=(description, func_name)
        self.options = {}

    def get_upper_bound(self):
        return len(self.options)

    def call_function_by_name(self, func_name: str, func_ref, *args, **kwargs):
        if func_name:
            return func_ref(*args, **kwargs)
        raise ValueError(f"Function '{func_name}' is not defined.")

    def load_options(self, path_name):
        try:
            with open(path_name, 'r') as input_file:
                for idx, line in enumerate(input_file):
                    result = [item.strip() for item in line.split(".") if item.strip()]
                    if len(result) >= 2:
                        self.options[idx] = (result[0], result[1])
        except Exception as e:
            print(f"Failed to load options from {path_name}: {e}")

    def __str__(self):
        return str(self.options)