from gql import gql
from dds import client as dds_client

key1 = (
    "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDegVP0JTtN5+7"
    "qgi7vb8pJ6kZvVEDFj/XtziAxpQF0JHq0ZsdrcPF5IKFA5s3py8"
    "F6g3/Vdu762sL/1hZFC9NCBfQWw2qbpTVq4vE78X9WPpt9sO5pA"
    "0+6y33rnjPFBxXYkpaFWgnyVjnAjAwPDNpCaY5vr+FzvSRdSKpk"
    "ws+vzg1sHAxoU008FMYsLxb6qVbU/+9fPe9Zl7g8CLbnnWUgqyH"
    "tIwVD37yDNIBBItCmzaDR2J2sH2zisEwpISVjIOsK964kYqWDi6"
    "YnayMx9DVOueUc9LIHv7tXjunqB5+EkSyT3bq0+2tHDhMJhJzFs"
    "bEt9+Tjvz9+cOmw+om1tZvD user2@example.com"
)

key2 = (
    "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC9HuXvYJPtQE/o"
    "/7TYi63yAopsrJ6TP+lDGdyQ+nVVp+5ojAIy9h8/h99UlNxjkiFT"
    "2YhI3Fl/pgNDRO4PVo6tlgb3CwiAZjSdeE5RnF79Dkj5XsM4j+FL"
    "MoXtbRw0K9ok9RKjz6ygIs1JDmaOdXexFnq4nAYU3fSLUa6Woccq"
    "THe8bFuJoAv1gbnx09Js8YcVMD96mpTJ3V/MK5YfIv10dbtrDhGu"
    "g3IS1V2J+0BB9orbQja554N+4S0I9rFBgVCpvPmQqddDHd/AdGkL"
    "v/zjEfGytjnvp68bEfDinkQkPfuxw01yd5MbcvLv39VVICWtKbqW"
    "263HT5LvSxwKorR7 user2@example.com"
)

keys = "\n".join((key1, key2))

update_ssh_keys_mutation = gql(
    """
    mutation UpdateSSHKeys ($keys: String!) {
        updateSshKeys(keys: $keys) {
            ok
            error
        }
    }
    """
)

result = dds_client.execute(update_ssh_keys_mutation, {"keys": keys})["updateSshKeys"]

print(f"success: {result['ok']}")
print(f"error: {result['error']}")
