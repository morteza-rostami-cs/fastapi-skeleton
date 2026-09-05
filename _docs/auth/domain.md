<!--

## add a flag to user model -- email_verified -- so we know who is verified

## email is user main identity

## username for now is some randomly generated server value.

## Token
   token
   user_id
   expires_at

   # this is for email verification
   # we store the hash of token in db

## Session
   session_id
   user_id
   expires_at
   created_at

   # browser gets the session_id -- inside cookie
   # store session in postgres



-->

```python

# add a server default value to migration -- if we already have data in our table -- otherwise: adding new col fails in migration

op.add_column(
    "user",
    sa.Column(
        "email_verified",
        sa.Boolean(),
        nullable=False,
        server_default=sa.false(), # add this line
    ),
)

```
