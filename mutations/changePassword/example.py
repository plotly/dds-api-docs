import gql
import dds_client

current_password = "current-password"
new_password = "new-password"

change_password_mutation = gql(
    """
    mutation {
        changePassword(currentPassword: {current_password}, newPassword: {new_password}) {
            ok
            currentPasswordError
            newPasswordError
        }
    }
    """
)

result = dds_client.execute(change_password_mutation)

print(f"success: {result.ok}")
print(f"current password error: {result.currentPasswordError}")
print(f"new password error: {result.newPasswordError}")
