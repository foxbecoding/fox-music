<template>
    <v-dialog
        v-if="dialog"
        v-model="dialog"
        persistent
        max-width="320"
    >
        <v-card class="auth-card">
            <v-card-title>{{dialogTitle}}</v-card-title>
            <v-form
                v-if="dialogType == 'create' || dialogType == 'update'"
                class="mb-4 mx-4"
                ref="form"
                v-model="valid"
                lazy-validation
            >
                <v-text-field
                    v-model="title"
                    :rules="titleRules"
                    label="Title*"
                    type="text"
                    required
                />

                <v-text-field
                    v-if="dialogType == 'create'"
                    v-model="yt_url"
                    :rules="yt_urlRules"
                    label="YouTube Url*"
                    type="text"
                    required
                />

                <v-select
                    v-model="selectedGenre"
                    :items="genres"
                    item-text="name"
                    item-value="uniqid"
                    :rules="selectedGenreRules"
                    label="Select genre"
                    required
                />  
                <v-select
                    v-model="selectedArtists"
                    :items="artists"
                    item-text="name"
                    item-value="uniqid"
                    label="Select artists"
                    :rules="selectedArtistsRules"
                    deletable-chips
                    multiple
                    required
                    chips
                />
            </v-form>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="close" text color="blue">Close</v-btn>
                <v-btn @click="submit" text color="blue">Submit</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>
<script lang="ts">
import { $axios } from '~/utils/api';
import Cookies from 'universal-cookie';
import Song from '~/utils/types/Songs';
import Genre from '~/utils/types/Genres';
import Artist from '~/utils/types/Artists';
import { RootState } from '@/store/index';
import { defineComponent, ref, watch, useStore, PropType} from '@nuxtjs/composition-api';

export default defineComponent({
    props: {
      showDialog: {
        type: Boolean,
        required: true
      },
      dialogType: {
        type: String,
        required: true
      },
      dialogTitle: {
        type: String,
        required: true
      },
      song: {
        type: Object as PropType<Song>,
        required: true
      },
      genres: {
        type: Array as PropType<Genre[]>,
        required: true
      },
      artists: {
        type: Array as PropType<Artist[]>,
        required: true
      }
    },
	setup(props, context) {
        const store = useStore<RootState>();
        const form = ref();
        const valid = ref<boolean>(true);
        const dialog = ref<boolean>(false);
        const title = ref<string>('');
        const titleRules = ref<any[]>([
            (v: any) => !! v || 'Song title is required'
        ]);
        const yt_url = ref<string>('');
        const yt_urlRules = ref<any[]>([
            (v: any) => !! v || 'YouTube url is required'
        ]);
        const selectedGenre = ref<string>('');
        const selectedGenreRules = ref<any>([
            (v: any) => !! v || 'Genre is required'
        ]);
        const selectedArtists = ref<string[]>([]);
        const selectedArtistsRules = ref<any[]>([
            (v: any) => v.length > 0 || 'Artists is required'
        ]);

        watch(props, () => {
            dialog.value = props.showDialog
            title.value = props.dialogType == 'update' ? props.song.title : '';
            selectedGenre.value = props.dialogType == 'update' ? props.song.genre.uniqid : '';
            selectedArtists.value = props.dialogType == 'update' ? props.song.artists.map(artist => artist.uniqid) : [];
        });

        //methods
         const submit = async () => {
            const cookies: Cookies = new Cookies();
            const csrftoken: string = cookies.get('csrftoken');  
            const auth_token: string = store.state.auth_token;
            if(props.dialogType == 'create'){
                create(csrftoken, auth_token)
            }else if(props.dialogType == 'update'){
                update(csrftoken, auth_token)
            }else{
                destroy(csrftoken, auth_token)
            }                    
        };

        const create = async (csrftoken: string, auth_token: string): Promise<void> => {
            if(!validate()){ return };
            interface PostData {
                title: string;
                yt_url: string;
                genre: string;
                artists: string[];
            }
            let postData: PostData = {
                title: title.value,
                yt_url: yt_url.value,
                genre: selectedGenre.value,
                artists: selectedArtists.value
            }

            try {
                const res = await $axios.$post(`${process.env.songsAPI}`, postData, {
                    progress: true,
                    withCredentials: true,
                    headers: {
                        'accept': 'application/json',
                        'Content-Type': `application/json`,
                        "X-CSRFToken": csrftoken, 
                        "Authorization": "Token "+auth_token
                    }
                });
                context.emit('refreshData')
                store.commit('snackbar', {text: res.success_message, show: true})
            } catch (error) {
                console.log(error) 
            } 
        };

        const update = async (csrftoken: string, auth_token: string): Promise<void> => {
            if(!validate()){ return };
            interface PostData {
                title: string;
                genre: string;
                artists: string[];
            }
            const postData: PostData = {
                title: title.value,
                genre: selectedGenre.value,
                artists: selectedArtists.value
            }

            try {
                const res = await $axios.$put(`${process.env.songsAPI+props.song.uniqid}/`, postData, {
                    progress: true,
                    withCredentials: true,
                    headers: {
                        'accept': 'application/json',
                        'Content-Type': `application/json`,
                        "X-CSRFToken": csrftoken, 
                        "Authorization": "Token "+auth_token
                    }
                });
                context.emit('refreshData')
                store.commit('snackbar', {text: res.success_message, show: true})
            } catch (error) {
                console.log(error); 
            }
        };
        
        const destroy = async (csrftoken: string, auth_token: string): Promise<void> => {
            try {
                const res = await $axios.$delete(`${process.env.songsAPI+props.song.uniqid}/`, {
                    progress: true,
                    withCredentials: true,
                    headers: {
                        'accept': 'application/json',
                        'Content-Type': `application/json`,
                        "X-CSRFToken": csrftoken, 
                        "Authorization": "Token "+auth_token
                    }
                });
                context.emit('refreshData')
                store.commit('snackbar', {text: res.success_message, show: true})
            } catch (error) {
                console.log(error); 
            }  
        };

        const close = (): void => {
            if(props.dialogType == 'create' 
            || props.dialogType == 'update'){ 
                reset(); 
            } 
            context.emit('close', false);
        }; 

        const validate = () => {
            return form.value.validate();
        };
        
        const reset = (): void => {
            form.value.reset();
            form.value.resetValidation();
        };
        
		return {
            form,
            valid,
            dialog,
            title,
            titleRules,
            yt_url,
            yt_urlRules,
            selectedGenre,
            selectedGenreRules,
            selectedArtists,
            selectedArtistsRules,
            close,
            submit,
		};
	},
})
</script>