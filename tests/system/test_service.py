from linux_parsers.parsers.system.service import parse_service


def test_service():
    command_output = """
[ + ]  apache2
[ - ]  bluetooth
[ ? ]  docker
    """
    parsed_output = parse_service(command_output)
    assert parsed_output == [{'service': 'apache2', 'status': 'running'},
                             {'service': 'bluetooth', 'status': 'stopped'},
                             {'service': 'docker', 'status': 'unknown'}]