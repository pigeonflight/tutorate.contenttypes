from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Item

from plone.directives import dexterity, form
from plone.app.textfield import RichText

from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable
from Products.ATContentTypes.interface import IATFolder

from tutorate.contenttypes import MessageFactory as _


# Interface class; used to define content-type schema.

class ISession(form.Schema, IImageScaleTraversable):
    """
    Session
    """

    # If you want a schema-defined interface, delete the model.load
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/session.xml to define the content type.

    #form.model("models/session.xml")
    topics = RichText(
            title=_(u"Topics"),
            description=_(u"areas to be covered"),
            required=False,
        ) 
    audience = RichText(
            title=_(u"Audience"),
            description=_(u"Your intended audience (e.g. startups, business persons, educators, web designers, programmers etc..)"),
            required=False,
        )
    sign_up_url = schema.Text(
            title=_(u"Sign Up URL"),
            description=_(u"URL to a sign up form"),
            required=False,
        )
    details = RichText(
            title=_(u"Details"),
            description=_(u"a more detailed overview"),
            required=False,
        )

    image = NamedBlobImage(
        title=_(u"Profile picture"),
        required=False,
    )



# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Session(Item):
    grok.implements(ISession)

    # Add your class methods and properties here
    pass


# View class
# The view will automatically use a similarly named template in
# session_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SessionListing(grok.View):
    grok.context(IATFolder)
    grok.require('zope2.View')

class View(grok.View):
    """ session view class """

    grok.context(ISession)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here