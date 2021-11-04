bl_info = {
    "name": "Setup Draw Texture",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy

class SetupDrawTexture(bpy.types.Operator):
    """My Setup Draw Texture Script"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.setup_draw_texture"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Setup Draw Texture"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):        # execute() is called when running the operator.
        bpy.ops.object.gpencil_add(location=(2.5, 0, 2.5))
        # bpy.data.cameras[0].location = (0, 8, 0)
        # bpy.context.camera.location = (0, 8, 0)
        return {'FINISHED'}            # Lets Blender know the operator finished successfully.

def menu_func(self, context):
    self.layout.operator(SetupDrawTexture.bl_idname)

def register():
    bpy.utils.register_class(SetupDrawTexture)
    bpy.types.TOPBAR_MT_render.append(menu_func)  # Adds the new operator to an existing menu.

def unregister():
    bpy.utils.unregister_class(SetupDrawTexture)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()