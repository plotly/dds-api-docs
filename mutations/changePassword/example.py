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

print("success: {result.ok}")
print("current password error: {result.currentPasswordError}")
print("new password error: {result.newPasswordError}")
