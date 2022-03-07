import herois

def initialize(context):
    """Inicializa Herois"""
    context.registerClass(
        herois.Herois,
        constructors = (
            herois.manage_addHeroisForm,
            herois.manage_addHerois,
            herois.nav,
            herois.foot,
            herois.Herois.style,
        ),
        icon = None
    )