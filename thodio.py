from IPython.core.display import display, Javascript


def thodio(line):
    jsstring = """
        (function() {
          var run = function() {
            if (window.displayThodio) {
              window.displayThodio("thodio_url")
            } else {
              setTimeout(run, 1000)
            }
          }
          run()
        })()
        """
    jsstring = jsstring.replace("thodio_url", line)
    display(Javascript(jsstring))


def load_ipython_extension(ipython):
    """This function is called when the extension is loaded.
    It accepts an IPython InteractiveShell instance.
    We can register the magic with the `register_magic_function`
    method of the shell instance."""
    ipython.register_magic_function(thodio, 'line')

