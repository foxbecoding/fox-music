<template>
    <div>
        <v-slider
            class="mx-0 musicplayer-slider"
            v-model="currentTime" 
            @end="end"
            @start="start"
            @input="mpSliderTime"
            color="red darken-2"
            :min="0"
            :max="duration"
            height="0"
            :ticks="false"
        >
        </v-slider> 
    </div>
</template>
<script lang="ts">
import { computed, defineComponent, ref, useStore, watchEffect} from '@nuxtjs/composition-api';
export default defineComponent({
	setup() {
        const currentTime = ref<Number>(0)
        const duration = ref<Number>(0)
        const store = useStore()

        //computed
        const AUDIO = computed(() => {
            return store.getters['MusicPlayer/audio']
        });
        const CURRENT_TIME = computed((): void => {
            currentTime.value = store.getters['MusicPlayer/currentTime']
        });
        const DURATION = computed((): void => {
            duration.value = store.getters['MusicPlayer/duration']
        });

        //watch
        watchEffect(() => {
            CURRENT_TIME.value
            DURATION.value
        })
        //methods
        const end = (e: number): void => { 
            store.commit('MusicPlayer/isSliding', false as boolean);
            AUDIO.value.currentTime = e;
        };

        const start = (e: number): void => { 
            store.commit('MusicPlayer/isSliding', true as boolean);
        };

        const mpSliderTime = (e: number): void => {
            store.commit('MusicPlayer/currentTimeStr', e)
        };

		return { 
            currentTime,
            duration,
            end,
            mpSliderTime,
            start,
		};
	}
})
</script>
<style scoped>
.musicplayer-slider{
    position: absolute;
    left: 0;
    top: 0px;
    width: 100%;
    height: 0px;
}
</style>

