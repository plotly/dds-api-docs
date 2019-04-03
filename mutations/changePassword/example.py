from gql import gql
import dds_client

change_password_mutation = gql(
    """
    mutation {
        changePassword(currentPassword: "current-password", newPassword: "new-password") {
            ok
            currentPasswordError
            newPasswordError
        }
    }
    """
)

result = dds_client.execute(change_password_mutation)["changePassword"]

print(f"success: {result['ok']}")
print(f"current password error: {result['currentPasswordError']}")
print(f"new password error: {result['newPasswordError']}")
