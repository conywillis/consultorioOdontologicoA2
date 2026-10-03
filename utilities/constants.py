class Constants:
    # Constants for client types
    PARTICULAR = "Particular"
    EPS = "EPS"
    PREPAGADA = "Prepagada"

    # Constants for attention types
    LIMPIEZA = "Limpieza"
    CALZA = "Calza"
    EXTRACCION = "Extracción"
    DIAGNOSTICO = "Diagnóstico"

    # Constants for attention priority
    NORMAL = "Normal"
    URGENTE = "Urgente"
    
    CLIENT_TYPES = [PARTICULAR, EPS, PREPAGADA]
    ATTENTION_TYPES = [LIMPIEZA, CALZA, EXTRACCION, DIAGNOSTICO]
    ATTENTION_PRIORITY = [NORMAL, URGENTE]