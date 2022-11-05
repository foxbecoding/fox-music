<template>
	<div class="musicplayer-mobile" v-show="IS_ACTIVE" :app="IS_ACTIVE">
        <LayoutsMusicPlayerMobileTimeSlider />
        <v-container>
            <LayoutsMusicPlayerMobileSongsDetails />
            <layoutsMusicPlayerMobileControls />
        </v-container>
    </div>
</template>
<script lang="ts">
import { computed, defineComponent, useStore} from '@nuxtjs/composition-api';
export default defineComponent({
	setup() {
        const store = useStore()

        //computed
        const IS_ACTIVE = computed<boolean>(
            () => store.getters['MusicPlayer/isActive']
        );     

		return { 
            IS_ACTIVE
		};
	}
})
</script>
<style scoped>
.musicplayer-mobile{
    width: 100%;
    height: 110px;
    background: rgb(12,12,12);
}
</style>

