from fasthtml.common import *
from random import randint

# for Docker
app, rt = fast_app(static_path="static")

# for local
# app, rt = fast_app(static_path="app/static")

default_header = Head(
                    Title("Bell Curve D20"),
                    Meta(charset="UTF-8"),
                    Meta(name="viewport", content="width=device-width, initial-scale=1"),
                    Meta(name="description", content="Roll d20 more reliably"),
                    Meta(name="author", content="EvenMoreH"),
                    Script(src="https://unpkg.com/htmx.org"),
                    Link(rel="stylesheet", href="css/tailwind.css"),
                    Link(rel="icon", href="images/favicon.ico", type="image/x-icon"),
                    Link(rel="icon", href="images/favicon.png", type="image/png"),
                )

crit = "20!"
miss = "1!"

@rt("/")
def homepage():
    return Html(
        default_header,
        Body(
            Div(
                Button("d20",
                    hx_get="d20",
                    hx_swap="innerHTML",
                    hx_target="#result",
                    cls="btn"),
                cls="flex justify-center mt-12"
            ),
            Div(
                Button("2d20",
                    hx_get="2d20",
                    hx_swap="innerHTML",
                    hx_target="#result",
                    cls="btn"),
                cls="flex justify-center"
            ),
            Div(
                id="result",
                cls="flex justify-center font-semibold text-6xl my-3"
            ),
            # whole body CSS
            cls="body"
        ),
    lang="en",
    )

@rt("/d20")
def get():
    a = randint(1, 8)
    b = randint(1, 12)
    d20 = a + b

    if d20 < 3:
        d20 = miss
    elif d20 > 18:
        d20 = crit
    else:
        d20 = d20

    return Div(d20)

@rt("/2d20")
def get():
    results = []

    for counter in range(0, 2):
        a = randint(1, 8)
        b = randint(1, 12)
        d20 = a + b

        if d20 < 3:
            d20 = miss
        elif d20 > 18:
            d20 = crit
        else:
            d20 = d20

        results.append(str(d20))
        dice = " & ".join(results)

    return Div(dice)


if __name__ == '__main__':
    # Important: Use host='0.0.0.0' to make the server accessible outside the container
    serve(host='0.0.0.0', port=5071)