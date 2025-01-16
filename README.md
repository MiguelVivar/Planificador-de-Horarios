# Planificador de Aulas y Horarios de Clases

## Descripción
Esta es una aplicación diseñada para facilitar la planificación y organización de horarios de clases en instituciones educativas. Permite optimizar el uso de aulas y recursos, asegurando que no haya conflictos en los horarios. Además, ofrece una interfaz gráfica amigable y funcional, con la posibilidad de exportar los datos en formato Excel, con tablas visualmente organizadas y coloreadas para mejorar la legibilidad.

---

## Características
- **Interfaz gráfica intuitiva**: Diseñada con `Tkinter` para facilitar la interacción del usuario.
- **Validación de datos**: Verifica que los datos ingresados sean correctos y estén completos.
- **Detección de conflictos**: Revisa los horarios para evitar conflictos de espacio y tiempo en las aulas.
- **Exportación a Excel**: Guarda los horarios en un archivo Excel con un formato limpio y profesional.
- **Compatibilidad con horarios complejos**: Manejo de múltiples aulas, días y horarios con gran precisión.

---

## Requisitos

### Tecnologías
- Python 3.8+
- Librerías adicionales:
  - `tkinter`: Para la creación de la interfaz gráfica.
  - `openpyxl`: Para la manipulación de archivos Excel.

### Instalación de librerías
Asegúrate de instalar las librerías necesarias ejecutando:
```bash
pip install openpyxl
```

---

## Estructura del Proyecto
```
HorariUN/
├── main.py                # Archivo principal de la aplicación
├── gui/
│   └── interfaz.py        # Módulo para la interfaz gráfica
├── modules/
│   ├── validador.py       # Lógica de validación de datos
│   ├── conflictos.py      # Verificación de conflictos en los horarios
│   └── excel.py           # Funciones para guardar datos en Excel
└── README.md              # Documentación del proyecto
```

---

## Uso

1. Ejecuta el archivo principal:
   ```bash
   python main.py
   ```

2. Ingresa los datos del curso:
   - Nombre del curso
   - Ciclo (I, II, III, ... X)
   - Sección (A, B, ...)
   - Día (Lunes, Martes, ...)
   - Horario de inicio y término
   - Salón
   - Tipo de clase (Teoría o Práctica)
   - Nombre del profesor

3. Haz clic en el botón **Validar y Guardar**:
   - Si hay un conflicto, se mostrará un mensaje de error en la interfaz.
   - Si los datos son válidos, el horario será guardado en el archivo Excel.

4. Los datos serán exportados automáticamente en un archivo Excel organizado.

---

## Contribución
Para mejorar o cambiar, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad (`git checkout -b nueva-funcionalidad`).
3. Realiza tus cambios y haz un commit (`git commit -m "Añadida nueva funcionalidad"`).
4. Haz un push a tu rama (`git push origin nueva-funcionalidad`).
5. Abre un pull request.

---

## Autores
**Miguel Vivar**   
GitHub: [MiguelVivar](https://github.com/MiguelVivar)
**Mario Muñoz**   
GitHub: [Mancilla](https://github.com/MiguelVivar)
**Luis Mitma**   
GitHub: [LuisMitma](https://github.com/MiguelVivar)
**Angielina Soto**   
GitHub: [Vinn](https://github.com/MiguelVivar)
**Anthony Palomino** 
GitHub: [Anthony](https://github.com/MiguelVivar)