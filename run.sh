# Busca un entorno de python
source bda_env/bin/activate
# Preparar BD
python init.py
echo 'Base de datos preparada'
# Clase y generación de monomios
python monomios.py
echo 'Monomios insertados'
# Clase y generación de polinomios
python polinomios.py
echo 'Polinomios insertados'
# Clase y generación de expresiones
python expresiones.py
echo 'Expresiones insertados'
# TODO: Poner los scripts que queden por correr acá

