<template>
    <v-container class="px-4" fluid>
        <v-card color="rgb(12,12,12)">
            <v-card-title>
                Songs 
                <v-spacer></v-spacer>
            </v-card-title>
            <v-data-table
                style="background: rgb(12,12,12)"
                :headers="headers"
                :items="songs"
                :search="search"
            >
                <template v-slot:top>
                    <v-toolbar flat color="rgb(18,18,18)">
                        <v-btn @click="create" depressed color="primary">
                            Add New Song
                        </v-btn>
                        <v-divider class="mx-4" inset vertical />
                        <v-spacer />
                        <v-text-field
                            v-model="search"
                            append-icon="mdi-magnify"
                            label="Search"
                            single-line
                            hide-details
                        /> 
                    </v-toolbar>
                </template>
                <template v-slot:item.thumbnail="{ item }">
                    <v-avatar rounded="lg" size="40">
                        <v-img 
                            :src="`/assets/song_thumbnails/${item.thumbnail}`"
                            width="40"
                            contain
                        />
                    </v-avatar>
                </template>
                <template v-slot:item.genre="{ item }">
                    {{item.genre.name}}
                </template>
                <template v-slot:item.artists="{item}">
                    <span 
                        v-for="(artist, a) in item.artists"
                        :key="`artist_${a}`"
                    >
                        <span>
                            {{artist.name}}
                        </span>
                        <span v-if="a < item.artists.length - 1">/</span>
                    </span>
                </template>
                <template v-slot:item.actions="{ item }">
                    <v-icon
                        small
                        class="mr-2"
                        color="warning"
                        @click="update(item)"
                    >
                        mdi-pencil
                    </v-icon>
                    <v-icon
                        small
                        color="red lighten-1"
                        @click="destroy(item)"
                    >
                        mdi-delete
                    </v-icon>
                </template>
            </v-data-table>
            <LibrarySongsManageList 
                @close="showDialog = false"
                @refreshData="refreshData"
                :showDialog="showDialog" 
                :dialogTitle="dialogTitle"
                :dialogType="dialogType"
                :song="selectedSong"
                :artists="artists"
                :genres="genres"
            />
        </v-card>
    </v-container>
</template>
<script lang="ts">
import Song from '~/utils/types/Songs';
import Genre from '~/utils/types/Genres';
import Artist from '~/utils/types/Artists';
import Headers from '~/utils/types/Library/Headers';
import { defineComponent, ref, PropType} from '@nuxtjs/composition-api';

export default defineComponent({
    props: {
      songs: {
        type: Array as PropType<Song[]>,
        required: true
      },
      genres: {
        type: Array as PropType<Genre[]>,
        required: true
      },
      artists: {
        type: Array as PropType<Artist[]>,
        required: true
      },
    },
	setup(props, context) {
        const search = ref<string>('');
        const dialogType = ref<string>('');
        const dialogTitle = ref<string>('');
        const showDialog = ref<boolean>(false);
        const selectedSong = ref<Song>({} as Song);
        const headers = ref<Headers[]>([
            { text: 'Thumbnail', value: 'thumbnail', align: 'start', sortable: false,},
            { text: 'Title', value: 'title', align: '', sortable: true, },
            { text: 'Artists', value: 'artists', align: '', sortable: true, },
            { text: 'Genre', value: 'genre', align: '', sortable: true, },
            { text: 'Actions', value: 'actions', align: 'end', sortable: false },
        ]);

        //methods
        const create = (): void => {
            showDialog.value = true;
            dialogType.value = 'create';
            dialogTitle.value = 'Add new song';
        };
        const update = (song: Song): void => {
            showDialog.value = true;
            selectedSong.value = song;
            dialogType.value = 'update';
            dialogTitle.value = 'Update song';
        };
        const destroy = (song: Song): void => {
            showDialog.value = true;
            selectedSong.value = song;
            dialogType.value = 'delete';
            dialogTitle.value = 'Are you sure that you want to delete this song?';
        };
        const refreshData = (): void => {
            context.emit('refresh')
            showDialog.value = false
        };
		return {
            search,
            headers, 
            showDialog,
            selectedSong,
            dialogType,
            dialogTitle,
            create,
            update, 
            destroy, 
            refreshData 
        };
	},
})
</script>
