from collections import deque

class Turno:

    def __init__(self):
        """
            Inicializa una instancia de la clase Turno 
            con tres colas segun la categoria y dos contadores 
            para la proporcion 3:2 de las categorias buena gente y cliente normal.
        """
        self.prioritario = deque()
        self.buena_gente = deque()
        self.cliente_normal = deque()
        self.max_buena_gente = 0
        self.max_cliente_normal = 0

    """ 
        Agrega un turno a la cola correspondiente según su categoría.

        Parámetros:
        id (int): El identificador del turno.
        categoria (str): La categoría del turno. 
        Puede ser 'Prioritario', 'Buena Gente' o 'Cliente Normal'.
    """
    def insertar_turno(self,id,categoria):
        if categoria == "Prioritario":
            self.prioritario.append(id)
        elif categoria == "Buena Gente":
            self.buena_gente.append(id)
        elif categoria == "Cliente Normal":
            self.cliente_normal.append(id)
        else:
            raise ValueError("No es posible identificar la Categoria")

    """
        Realizar el llamado del proximo turno segun su categoria.

        Retorna: El ID(int) del turno respectivo o un mensaje de "No hay proximos turnos"
        en caso de tener las colas vacias.

        Reglas:
        - Los turnos 'Prioritario' se atienden primero de forma consecutiva.
        - Si hay turnos 'Buena Gente' y 'Cliente Normal', se sigue una proporción 3:2.
        - Si solo hay turnos de un tipo, se atienden de manera consecutiva.
    """  
    def llamar_turno(self):
        if self.prioritario:
            return self.prioritario.popleft()
        
        if self.buena_gente and self.cliente_normal:
            if self.max_buena_gente<3:
                self.max_buena_gente+=1
                return self.buena_gente.popleft()
            elif self.max_cliente_normal<2:
                self.max_cliente_normal+=1
                return self.cliente_normal.popleft()
            else:
                self.max_buena_gente=0
                self.max_cliente_normal=0

        if self.buena_gente:
            return self.buena_gente.popleft()
        
        if self.cliente_normal:
            return self.cliente_normal.popleft()
        
        return ("No hay proximos turnos")
