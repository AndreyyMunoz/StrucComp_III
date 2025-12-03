# core/app_state.py

class AppState:
    """
    Singleton para mantener el estado global de la aplicación.
    Aquí vive el grafo actual, resultados recientes, etc.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            # Estado inicial
            cls._instance.graph = None
            cls._instance.last_matching = None
            cls._instance.U = None
            cls._instance.V = None

        return cls._instance

    def reset(self):
        """Resetea el estado (útil si se carga un grafo nuevo)."""
        self.graph = None
        self.last_matching = None
        self.U = None
        self.V = None
