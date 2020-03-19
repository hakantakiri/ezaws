#! /usr/bin/python3

# Importing packages
import argparse

# Importing settings
import settings

# Importing options
from options.aws_lambda.main import LambdaOption
from options.aws_apigateway.main import ApigatewayOption

# Declaring global variables
DESCRIPTION = settings.DESCRIPTION
PROG = settings.PROG
SUB_HELP = settings.SUB_HELP
SUB_DEST = settings.SUB_DEST

option_lambda = LambdaOption()
option_apigateway = ApigatewayOption()

options = [
            option_lambda,
            option_apigateway
        ]

# Building functions
def check_aliases_collisions():
    control_options = []
    flag = True
    for option in options:
        for alias in option.get_cli_aliases():
            if alias in control_options:
                flag = False
                print("Error: There is a collition, '{}' alias is found in two options".format(alias))
                exit()
            else :
                control_options.append(alias)

    return flag

def build_parser() :
    
    parser = argparse.ArgumentParser(description = DESCRIPTION)
    subparsers = parser.add_subparsers( help = SUB_HELP, dest = SUB_DEST)

    for option in options :
        option.build_subparser( subparsers )    

    args = parser.parse_args()
    
    return args

def execute_option( args ): 
    
    for option in options:
        if args.option == option.get_option_name() or args.option in option.get_cli_aliases() :
            option.execute_command( args.command, args)
    

# Main function

def main():
    check_aliases_collisions ()
    args = build_parser()
    print(args )
    execute_option( args )




if __name__ == '__main__':
    main()