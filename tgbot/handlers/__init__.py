"""Import all routers and add them to routers_list."""
from .users import admin_router, user_router, echo_router
from .groups import edit_group_router, group_moderator_router, service_messages_router

routers_list = [
    admin_router,
    user_router,
    edit_group_router, 
    group_moderator_router, 
    service_messages_router,
    echo_router,  # echo_router must be last
]

__all__ = [
    "routers_list",
]