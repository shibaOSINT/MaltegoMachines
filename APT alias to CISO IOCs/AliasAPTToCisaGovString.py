from extensions import registry
from maltego_trx.entities import Phrase, Alias
from maltego_trx.maltego import MaltegoMsg, MaltegoTransform

from maltego_trx.transform import DiscoverableTransform


@registry.register_transform(display_name="To CISA gov search string", input_entity=Alias,
                             description='Output a phrase Entity to search this APT in a CISA advisory using a search '
                                         'engine',
                             output_entities=[Phrase])
class AliasAPTToCisaGovString(DiscoverableTransform):

    @classmethod
    def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):
        apt_name = request.Value
        search_str = f'"{apt_name}" cisa.gov'
        response.addEntity(type=Phrase, value=search_str)
