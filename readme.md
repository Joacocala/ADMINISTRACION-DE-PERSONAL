# Administración de Personal en Django

Este proyecto es una aplicación web desarrollada con Django, diseñada para facilitar la gestión eficiente del personal en organizaciones. A continuación, se detallan sus principales características y funcionalidades.

## Autenticación

La autenticación es un componente fundamental de la aplicación. Para acceder a las distintas vistas y realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los colaboradores, es necesario iniciar sesión con credenciales válidas. Esto garantiza que solo los usuarios autorizados puedan gestionar la información del personal.

## Otros
Se utiliza la herencia HTML en los casos necesarios.

## Sistema de Alta, Baja y Modificación (ABM) de Colaboradores

La aplicación incluye un sistema robusto para el ABM de colaboradores. Los usuarios pueden:

- **Registrar** nuevos empleados en el sistema, proporcionando detalles relevantes como nombre, posición, zona, etc.
- **Modificar** los perfiles de los empleados existentes, actualizando su información según sea necesario.
- **Eliminar** registros de empleados que ya no forman parte de la organización.

## Registro y Modificación de Perfiles de Usuarios

Además del sistema de ABM para colaboradores, la aplicación también permite a los usuarios registrarse y modificar sus propios perfiles. Esto incluye cambiar contraseñas, actualizar información de contacto y más.

## Funcionalidades Futuras

Aunque actualmente no están en producción, el proyecto contempla la integración de aplicaciones adicionales relacionadas con el seguimiento de inventario (BASE) y la gestión de flotas vehiculares (FLOTA). Estas funcionalidades estarán disponibles en versiones futuras de la aplicación.

## Conclusión

La administración de personal en Django ofrece una solución integral para la gestión de recursos humanos, combinando facilidad de uso con seguridad y flexibilidad. Con su sistema de autenticación, ABM de colaboradores y capacidades de registro y modificación de perfiles, esta aplicación es una herramienta valiosa para cualquier organización que busque optimizar sus procesos de gestión de personal.

Para comenzar a utilizar la aplicación, sigue las instrucciones de instalación y configuración proporcionadas en el repositorio.

## Ejecucion
Clona el repositorio en tu ordenador.
  1) Ejecuta las migraciones necesarias e instala DJANGO &  Pillow
  2)Ejecuta las migraciones con el comando python manage.py migrate.
  3)Inicia el servidor con el comando python manage.py runserver.
  4)Abre tu navegador y navega a http://localhost:8000 para ver la aplicación en acción.



