<template>
	<div>
		<v-container class="px-4 pb-0" fluid>
			<h2>{{title}}</h2>
		</v-container>
		<v-container 
			:class="$vuetify.breakpoint.mdAndUp ? 'px-4' : 'px-0'" 
			class="pt-1" 
			fluid
		>
			<v-list color="rgb(3,3,3)">
				<v-list-item-group v-model="model">
					<v-divider />
					<div
						v-for="(song, i) in songs"
						:key="`song_${i}`"
						@click="selectSong(song)"
					>
						<v-list-item link>
							<v-list-item-avatar rounded="lg">
								<v-img 
									:src="`/assets/song_thumbnails/${song.thumbnail}`"
									contain
								/>
							</v-list-item-avatar>
							<v-list-item-content>
								<v-list-item-title>
									{{song.title}}
								</v-list-item-title>
								<v-list-item-title v-if="$vuetify.breakpoint.smAndDown">
									<span 
										v-for="(artist, a) in song.artists"
										:key="`artist_${a}`"
									>
										<span
											@click.stop="$router.push(`/artists/${artist.uniqid}`)" 
											class="artist-name"
										>{{artist.name}}</span>
										<span v-if="a < song.artists.length - 1"> / </span>
									</span>		
								</v-list-item-title>
							</v-list-item-content>
							<v-list-item-content v-if="$vuetify.breakpoint.mdAndUp">
								<v-list-item-title>
									<span 
										v-for="(artist, a) in song.artists"
										:key="`artist_${a}`"
									>
										<span
											@click.stop="$router.push(`/artists/${artist.uniqid}`)" 
											class="artist-name"
										>{{artist.name}}</span>
										<span v-if="a < song.artists.length - 1"> / </span>
									</span>		
								</v-list-item-title>
							</v-list-item-content>
							<v-spacer />
							<v-list-item-action>
								<v-btn @click.stop :to="`/genres/${song.genre.uniqid}`" width="60" x-small outlined color="blue">
									{{song.genre.name}}
								</v-btn>
							</v-list-item-action>
						</v-list-item>			
						<v-divider />
					</div>
				</v-list-item-group>
			</v-list>
		</v-container>
	</div>	
	
</template>
<script lang="ts">
import { 
	defineComponent, 
	PropType, 
	useStore, 
	ref, 
	watch,
	watchEffect, 
	computed,
	useRoute
} from '@nuxtjs/composition-api';
import { MusicPlayerState } from '~/store/MusicPlayer';
import Song from '~/utils/types/Songs';
export default defineComponent({
	props: {
      songs: {
        type: Array as PropType<Song[]>,
        required: true
      },
      title: {
        type: String,
        required: false
      }
    },
	setup(props) {
		const model = ref<any>(null);
		const store = useStore<MusicPlayerState>();
		const route = useRoute();

		//computed
		const SONG = computed<Song>( 
            () => store.getters['MusicPlayer/song']
        );

		//methods
		const selectSong = (song: Song): void => {
			store.commit('MusicPlayer/isActive', true as boolean);
			store.commit('MusicPlayer/isShuffled', false as boolean);
			store.commit('MusicPlayer/song', song as Song);
			store.commit('MusicPlayer/songs', props.songs as Song[]);
			store.commit('MusicPlayer/songsConst', props.songs as Song[]);
			store.commit('MusicPlayer/audio', `/assets/songs/${song.filename}` as string);
		};

		const setModelValue = (): void => {
			let song_index: number = props.songs.findIndex(song => song.uniqid == SONG.value.uniqid);
			model.value = song_index;
		};

		//watchers
    watch(SONG, () => {
        setModelValue();
    });

		watchEffect(() => {
			setModelValue();
		});
	
		return {
			model,
			selectSong
		};
	}
})
</script>
<style scoped>
.artist-name:hover{
	cursor: pointer;
	color: #2196F3;
}
</style>
