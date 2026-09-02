const UserCard = {
  template: /*html*/ `
        <div class="bg-white border rounded-xl p-4 shadow-sm">

            <div class="flex items-center justify-between">

                <div>
                    <h2 class="font-bold text-lg">
                        {{ name }}
                    </h2>

                    <p class="text-gray-500 text-sm">
                        {{ description }}
                    </p>
                </div>

                <div class="text-2xl">
                    👤
                </div>

            </div>

        </div>
    `,

  props: {
    name: {
      type: String,
      required: true,
    },

    description: {
      type: String,
      default: "User",
    },
  },
};
