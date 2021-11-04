bl_info = {
    "name": "Render grease pencil",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy

class SetupDrawTexture(bpy.types.Operator):
    """My Render Script"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.setup_draw_texture"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Render grease pencil"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def hideAllLayers():
        layers = bpy.data.grease_pencils[0].layers  
        for layer in layers:
            layer.hide = True
    def execute(self, context):        # execute() is called when running the operator.
        # GP
        layers = bpy.data.grease_pencils[0].layers  
        # Assume the last argument is image path
        for i in range(len(layers)):
            layer = layers[i]
            # print(layer.info)
            self.hideAllLayers()
            layer.hide = False
            bpy.context.scene.render.filepath = "{}/__{}__{}.png".format('.', i ,layer.info)
            bpy.ops.render.render(write_still=True)
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