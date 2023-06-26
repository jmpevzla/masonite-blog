"""CreatePostsTable Migration."""

from masoniteorm.migrations import Migration


class CreatePostsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("posts") as table:
            table.big_increments("id")
            table.string("title")
            
            table.big_integer("author_id").unsigned()
            table.foreign("author_id").references("id").on("users")

            table.string("body")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("posts")
