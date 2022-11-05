<template>
    <div class="text-center">
        <v-snackbar
            v-model="show"
            color="rgb(20,20,20)"
            @input="close"
        >
            {{ text }}
            <template v-slot:action="{ attrs }">
                <v-btn
                    color="blue"
                    text
                    v-bind="attrs"
                    @click="show = false"
                >
                Close
                </v-btn>
            </template>
        </v-snackbar>
    </div>
</template>
<script lang="ts">
import { defineComponent, computed, useStore, ref, watch} from '@nuxtjs/composition-api';

export default defineComponent({
	setup() {
        const store = useStore()
        const show = ref()
        const text = ref()
        const SHOW_SNACKBAR = computed(
            () => store.getters['show_snackbar']
        );
        const SNACKBAR_TEXT = computed(
            () => store.getters['snackbar_text']
        );
        const close = (e: boolean) => {
            store.commit('snackbar', {text: '', show: e})
        };
        watch(SHOW_SNACKBAR, () => {
            show.value = SHOW_SNACKBAR.value
            text.value = SNACKBAR_TEXT.value
        })
		return { show, text, close };
	},
})
</script>
