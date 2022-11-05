<template>
    <v-card class="auth-card" color="rgb(10,10,10)" max-width="400" flat>
        <v-card-title>Sign In</v-card-title>
            <v-form
                class="mb-4 mx-4"
                ref="form"
                v-model="valid"
                lazy-validation
            >
                <v-text-field
                    v-model="username"
                    :rules="usernameRules"
                    label="Username*"
                    type="text"
                    required
                    @keyup.enter="submit"
                ></v-text-field>

                <v-text-field
                    v-model="password"
                    :rules="passwordRules"
                    label="Password*"
                    type="password"
                    required
                    @keyup.enter="submit"
                ></v-text-field>  
                <v-btn @click="submit" color="blue">Sign in</v-btn>
        </v-form>
    </v-card>
</template>
<script lang="ts">
import { RootState } from '@/store';
import { $axios } from '~/utils/api';
import Cookies from 'universal-cookie';
import { defineComponent, ref, useStore, useRouter} from '@nuxtjs/composition-api';
export default defineComponent({
	setup() {
        const router = useRouter();
        const store = useStore<RootState>();
        const form = ref();
        const valid = ref<boolean>(true);
        const username = ref<string>('');
        const usernameRules = ref<any[]>([
            (v: any) => !! v || 'Username is required'
        ]);
        const password = ref<string>('');
        const passwordRules = ref<any[]>([
            (v: any) => !! v || 'Username is required'
        ]);

        //methods
         const submit = async () =>{
            if(!validate()){ return }
            interface PostData {
                username: string;
                password: string;
            };
            const post_data: PostData  = {
                username: username.value, 
                password: password.value
            };
            const cookies = new Cookies();
            const csrftoken = cookies.get('csrftoken'); 
            try {
                const res = await $axios.$post(`${process.env.authAPI}`, post_data, {
                    progress: true,
                    withCredentials: true,
                    headers: {
                        'accept': 'application/json',
                        'Content-Type': `application/json`,
                        "X-CSRFToken": csrftoken, 
                    }
                });
                store.commit('auth_token', res.token);
                router.replace('/library');
            } catch (error) {
                console.log(error); 
            }                           
        };
        const validate = () => {
            return form.value.validate();
        };
        const reset = (): void => {
            form.value.reset();
        };
        const resetValidation = (): void => {
            form.value.resetValidation();
        };
        
		return {
            form,
            valid,
            username,
            password,
            usernameRules,
            passwordRules,
            reset,
            submit
		};
	}
})
</script>
<style scoped>
.auth-card{
    position: absolute;
    width: 100%;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
</style>
