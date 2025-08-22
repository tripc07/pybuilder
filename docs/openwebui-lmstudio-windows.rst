Open WebUI and LM Studio on Windows 11
=====================================

This guide provides a minimal setup for deploying `Open WebUI <https://github.com/open-webui/open-webui>`_
connected to `LM Studio <https://lmstudio.ai>`_ on a Windows 11 machine without
Docker. ``uv`` manages a lightweight Python environment and installs the
required packages. The result is a local, self‑hosted chat UI that can use
models served by LM Studio through its OpenAI‑compatible API.

Prerequisites
-------------

* Windows 11 with administrator access.
* An Internet connection for initial downloads.
* ``uv`` installed. Install by running ``iwr https://astral.sh/uv/install.ps1 | iex`` in PowerShell.

Step 1 – Install LM Studio
-------------------------

1. Download the latest **LM Studio** installer for Windows from
   https://lmstudio.ai and run the setup program.
2. Launch LM Studio and, from the *Settings → Developer* section,
   enable the **OpenAI Compatible API Server**.
3. Note the API server port shown (default: ``1234``). LM Studio will now
   listen on ``http://localhost:1234/v1`` for API requests.

Step 2 – Install and run Open WebUI with ``uv``
---------------------------------------------

1. Open **PowerShell**, create a virtual environment, and install Open WebUI:

   .. code-block:: powershell

      uv venv webui
      uv pip install open-webui

2. Point Open WebUI at the LM Studio API server and start it:

   .. code-block:: powershell

      $env:OPENAI_API_BASE = "http://localhost:1234/v1"
      $env:OPENAI_API_KEY = "lm-studio"
      uv run open-webui serve --host 0.0.0.0 --port 3000

   The server listens on port ``3000`` and proxies requests to LM Studio.

Step 3 – Add PyBuilder for testing (optional)
--------------------------------------------

Install PyBuilder in the same ``uv`` environment to run project tests:

.. code-block:: powershell

   uv pip install pybuilder
   uv run pyb -v  # or: uv run pytest

Step 4 – Access the UI
----------------------

* Open a browser to ``http://localhost:3000``.
* Create the initial administrator account when prompted.
* Chat with models served by LM Studio.

Maintenance
-----------

* Update packages with ``uv pip install --upgrade open-webui pybuilder``.
* Stop the server with ``Ctrl+C`` and restart using ``uv run open-webui serve``.

This setup keeps all components self‑contained and requires only ``uv`` and
LM Studio on the host, providing an easy entry point for local experimentation
with LLMs.
