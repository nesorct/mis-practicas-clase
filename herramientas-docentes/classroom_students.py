#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para obtener la lista de alumnos de Google Classroom
"""

import os
import sys

# Configurar encoding para Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes necesarios: ver cursos, ver alumnos, ver/modificar tareas y notas
SCOPES = [
    'https://www.googleapis.com/auth/classroom.courses.readonly',
    'https://www.googleapis.com/auth/classroom.rosters.readonly',
    'https://www.googleapis.com/auth/classroom.coursework.students'
]

# Ruta al archivo de credenciales
CREDENTIALS_FILE = 'client_secret_795247858815-p895ptdoca7ol3kmrgvdu0gapn37nrvf.apps.googleusercontent.com.json'

def authenticate():
    """Autentica con Google y devuelve las credenciales."""
    creds = None

    # El archivo token.json guarda las credenciales del usuario
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # Si no hay credenciales validas, pedir autorizacion
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=8080)

        # Guardar las credenciales para la proxima vez
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

def get_courses(service):
    """Obtiene la lista de cursos del profesor."""
    results = service.courses().list().execute()
    courses = results.get('courses', [])

    print("\n[CURSOS DISPONIBLES]")
    print("-" * 60)
    for i, course in enumerate(courses, 1):
        print(f"{i}. {course['name']}")
        print(f"   ID: {course['id']}")
        print(f"   Seccion: {course.get('section', 'N/A')}")
    print("-" * 60)

    return courses

def get_students(service, course_id):
    """Obtiene la lista de estudiantes de un curso."""
    students = []
    page_token = None

    while True:
        response = service.courses().students().list(
            courseId=course_id,
            pageToken=page_token
        ).execute()

        students.extend(response.get('students', []))
        page_token = response.get('nextPageToken')

        if not page_token:
            break

    return students

def main():
    print("=" * 60)
    print("OBTENER ALUMNOS DE GOOGLE CLASSROOM")
    print("=" * 60)

    # Autenticar
    print("\nAutenticando con Google...")
    print("Se abrira el navegador para que autorices el acceso.")
    print("Inicia sesion con: jaime.aniorte@murciaeduca.es")
    creds = authenticate()
    print("Autenticacion exitosa!")

    # Crear servicio
    service = build('classroom', 'v1', credentials=creds)

    # Obtener cursos
    courses = get_courses(service)

    if not courses:
        print("\nNo se encontraron cursos.")
        return

    # Seleccionar curso
    print("\nIntroduce el NUMERO del curso que quieres:")
    course_num = input("> ").strip()

    if course_num.isdigit():
        idx = int(course_num) - 1
        if 0 <= idx < len(courses):
            course_id = courses[idx]['id']
            course_name = courses[idx]['name']
        else:
            print("Numero invalido.")
            return
    else:
        print("Introduce solo el numero.")
        return

    # Obtener estudiantes
    print(f"\nObteniendo lista de alumnos de: {course_name}...")
    students = get_students(service, course_id)

    print("\n" + "=" * 60)
    print(f"LISTA DE ALUMNOS ({len(students)} alumnos)")
    print("=" * 60)

    student_names = []
    for i, student in enumerate(students, 1):
        profile = student.get('profile', {})
        name = profile.get('name', {})
        full_name = f"{name.get('givenName', '')} {name.get('familyName', '')}".strip()
        email = profile.get('emailAddress', '')

        student_names.append(full_name.upper())
        print(f"{i:2}. {full_name} ({email})")

    # Guardar lista en archivo
    output_file = 'lista_alumnos_classroom.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        for name in student_names:
            f.write(name + '\n')

    print(f"\n[OK] Lista guardada en '{output_file}'")

    return student_names

if __name__ == '__main__':
    main()