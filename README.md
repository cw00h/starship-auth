# starship-auth

`starship-auth` supplies an authentication provider for the Starship command-line
application.

Set `STARSHIP_API_KEY` before starting the application. The provider checks the
configured credential with the Starship authentication service and exposes the
result through the `starship.auth` plugin interface.

Service documentation and status are available at
`https://api.starship-auth.com/docs` and
`https://api.starship-auth.com/health`.
