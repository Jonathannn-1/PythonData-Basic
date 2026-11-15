import flet as ft


def ejercicio_fstrings(nombre: str, edad: str) -> str:

    return f"Mi nombre es {nombre} y tengo {edad} años"


def ejercicio_condiciones(numero: str) -> str:

    try:
        num = int(numero)

        if num % 2 == 0:
            return f'numero ingresado es par {num}'
        else:
            return f'numero ingresado impar {num}'
    except ValueError:
        return 'El valor ingresado no es válido'


def ejercicio_quit(historial: list, nueva_entrada: str) -> tuple:

    entrada_limpia = nueva_entrada.strip()

    if entrada_limpia.lower() == 'salir':
        return [],'hasta luego, saliste!!'
    
    if entrada_limpia != '':
        historial.append(entrada_limpia)
    
    return historial, f"Historial actual: {historial}"

def ejercicio_diccionario(diccionario: dict, clave: str, valor: str) -> tuple:

    if clave.lower() == 'ver':
        return diccionario, f'Diccionario actual: {diccionario}'
    
    elif clave.lower() == 'limpiar':
        diccionario.clear()
        return diccionario,f'diccionario vaciodo con exito {diccionario}'

    elif clave.strip() != '' and valor.strip() != '':
        diccionario[clave.strip()] = valor.strip()
        return diccionario, f'clave {clave.strip()} agregada con exito '



    return diccionario, "Completa el ejercicio del diccionario"


def main(page: ft.Page):
    page.title = "Pildoras de Programacion - Practica"
    page.bgcolor = "#0f0f0f"
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
    page.window.width = 820
    page.window.min_width = 700

    VERDE      = "#00c853"
    GRIS_CARD  = "#1a1a2e"
    GRIS_INPUT = "#16213e"
    TEXTO      = "#e0e0e0"
    SUBTEXTO   = "#9e9e9e"

    historial_quit   = []
    diccionario_data = {}

    def card(titulo, contenido):
        return ft.Container(
            content=ft.Column([
                ft.Text(titulo, size=16, weight=ft.FontWeight.BOLD, color=VERDE),
                ft.Divider(color="#2a2a4a", height=1),
                contenido,
            ], spacing=12),
            bgcolor=GRIS_CARD,
            border_radius=14,
            padding=20,
            border=ft.Border.all(1, "#2a2a4a"),
        )

    def output_box(ref):
        return ft.Container(
            content=ft.Text("", ref=ref, color=VERDE, size=13, selectable=True),
            bgcolor="#0a0a1a",
            border_radius=8,
            padding=ft.Padding(14, 10, 14, 10),
            border=ft.Border.all(1, "#2a2a4a"),
            height=50,
        )

    def campo(hint, ref, expand=True):
        return ft.TextField(
            hint_text=hint,
            ref=ref,
            expand=expand,
            bgcolor=GRIS_INPUT,
            border_color="#2a2a4a",
            focused_border_color=VERDE,
            color=TEXTO,
            hint_style=ft.TextStyle(color=SUBTEXTO),
            border_radius=8,
            height=42,
            text_size=13,
            content_padding=ft.Padding(12, 8, 12, 8),
        )

    def boton(texto, on_click):
        return ft.ElevatedButton(
            texto,
            on_click=on_click,
            bgcolor=VERDE,
            color="#000000",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
            height=42,
        )

    ref_nombre = ft.Ref[ft.TextField]()
    ref_edad   = ft.Ref[ft.TextField]()
    ref_out1   = ft.Ref[ft.Text]()

    def run_fstrings(e):
        resultado = ejercicio_fstrings(
            ref_nombre.current.value or "",
            ref_edad.current.value or "0"
        )
        ref_out1.current.value = resultado
        page.update()

    sec1 = card("F-Strings", ft.Column([
        ft.Text("Completa ejercicio_fstrings() y presiona Ejecutar", color=SUBTEXTO, size=12),
        ft.Row([campo("Tu nombre", ref_nombre), campo("Tu edad", ref_edad, expand=False)], spacing=10),
        boton("Ejecutar", run_fstrings),
        output_box(ref_out1),
    ], spacing=10))

    ref_num  = ft.Ref[ft.TextField]()
    ref_out2 = ft.Ref[ft.Text]()

    def run_condiciones(e):
        resultado = ejercicio_condiciones(ref_num.current.value or "0")
        ref_out2.current.value = resultado
        page.update()

    sec2 = card("Condiciones", ft.Column([
        ft.Text("Completa ejercicio_condiciones() y presiona Ejecutar", color=SUBTEXTO, size=12),
        ft.Row([campo("Ingresa un numero", ref_num), boton("Ejecutar", run_condiciones)], spacing=10),
        output_box(ref_out2),
    ], spacing=10))

    ref_quit = ft.Ref[ft.TextField]()
    ref_out3 = ft.Ref[ft.Text]()

    def run_quit(e):
        nonlocal historial_quit
        entrada = ref_quit.current.value or ""
        historial_quit, resultado = ejercicio_quit(historial_quit, entrada)
        if "Hasta luego" in resultado:
            historial_quit = []
        ref_out3.current.value = resultado
        ref_quit.current.value = ""
        page.update()

    sec3 = card("Letting the User Choose When to Quit", ft.Column([
        ft.Text('Escribe valores y envialos. Escribe "salir" para terminar.', color=SUBTEXTO, size=12),
        ft.Row([campo('Escribe algo o "salir"', ref_quit), boton("Enviar", run_quit)], spacing=10),
        output_box(ref_out3),
    ], spacing=10))

    ref_clave = ft.Ref[ft.TextField]()
    ref_valor = ft.Ref[ft.TextField]()
    ref_out4  = ft.Ref[ft.Text]()

    def run_dict(e):
        nonlocal diccionario_data
        clave = ref_clave.current.value or ""
        valor = ref_valor.current.value or ""
        diccionario_data, resultado = ejercicio_diccionario(diccionario_data, clave, valor)
        ref_out4.current.value = resultado
        ref_clave.current.value = ""
        ref_valor.current.value = ""
        page.update()

    sec4 = card("Filling a Dictionary", ft.Column([
        ft.Text('Agrega clave/valor. Escribe "ver" para ver el dict, "limpiar" para vaciarlo.', color=SUBTEXTO, size=12),
        ft.Row([campo("Clave", ref_clave), campo("Valor", ref_valor), boton("Agregar", run_dict)], spacing=10),
        output_box(ref_out4),
    ], spacing=10))

    header = ft.Container(
        content=ft.Row([
            ft.Image(
                src="https://picsum.photos/100", 
                width=56, height=56,
                border_radius=28,
            ),
            ft.Column([
                ft.Text("Pildoras de Programacion", size=20, weight=ft.FontWeight.BOLD, color=VERDE),
                ft.Text("Practica en vivo  -  while  -  break  -  continue  -  f-strings  -  condiciones", size=12, color=SUBTEXTO),
            ], spacing=2, expand=True),
        ], spacing=16),
        bgcolor=GRIS_CARD,
        padding=ft.Padding(28, 18, 28, 18),
        # CORREGIDO: Uso de la clase ft.Border directo con el parámetro bottom
        border=ft.Border(bottom=ft.BorderSide(1, "#2a2a4a")),
    )

    page.add(
        header,
        ft.Container(
            content=ft.Column([sec1, sec2, sec3, sec4], spacing=16),
            padding=ft.Padding(24, 24, 24, 24),
        )
    )


ft.app(target=main)