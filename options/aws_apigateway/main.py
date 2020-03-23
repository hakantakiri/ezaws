#! /usr/bin/python3

from options.aws_apigateway import constants

class ApigatewayOption:

    _option_name = constants.OPTION_NAME
    _cli_help =  constants.CLI_HELP
    _cli_choices = constants.CLI_CHOICES
    _cli_aliases = constants.CLI_ALIASES
       
    def get_option_name( self ) : 
        return self._option_name
    
    def get_cli_help ( self ) :
        return self._cli_help
    
    
    def get_cli_choices( self ) :
        return self._cli_choices

    def get_cli_aliases( self ) :
        return self._cli_aliases

    def build_subparser ( self, subparsers ):
        
        subparser_get_function =  subparsers.add_parser('get-model', help = "To download model" )
        subparser_get_function.add_argument('--model-name', type=str, required = True)
        subparser_get_function.add_argument('--profile', type=str, default = 'default')       