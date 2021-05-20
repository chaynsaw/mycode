def cmdissue(toissue, activesession):
      print(toissue)
      ssh_stdin, ssh_stdout, ssh_stderr = activesession.exec_command(toissue)
      return ssh_stdout.read().decode('UTF-8')

