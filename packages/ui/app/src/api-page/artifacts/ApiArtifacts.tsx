import { H2 } from "@blueprintjs/core";
import * as FernRegistryDocsRead from "@fern-fern/registry-browser/api/resources/docs/resources/v1/resources/read";
import { useApiDefinitionContext } from "../../api-context/useApiDefinitionContext";
import { joinUrlSlugs } from "../../docs-context/joinUrlSlugs";
import { PageMargins } from "../../page-margins/PageMargins";
import { useApiPageCenterElement } from "../useApiPageCenterElement";
import { ApiArtifactsTitle } from "./ApiArtifactsTitle";
import { DotNetLogo } from "./sdk-logos/DotNetLogo";
import { GoLogo } from "./sdk-logos/GoLogo";
import { JavaLogo } from "./sdk-logos/JavaLogo";
import { PythonLogo } from "./sdk-logos/PythonLogo";
import { RubyLogo } from "./sdk-logos/RubyLogo";
import { SdkCard } from "./SdkCard";
import { SdkCardLayout } from "./SdkCardLayout";

export declare namespace ApiArtifacts {
    export interface Props {
        apiArtifacts: FernRegistryDocsRead.ApiArtifacts;
    }
}

export const ApiArtifacts: React.FC<ApiArtifacts.Props> = ({ apiArtifacts }) => {
    const { apiSlug } = useApiDefinitionContext();
    const slug = joinUrlSlugs(apiSlug, "client-libraries");

    const { setTargetRef } = useApiPageCenterElement({ slug });

    return (
        <PageMargins>
            <div ref={setTargetRef}>
                <H2 className="pt-20">
                    <ApiArtifactsTitle />
                </H2>
                <div className="mt-5 text-lg text-neutral-400">
                    Official open-source client libraries for your favorite platforms.
                </div>
                <div className="mt-16 grid grid-cols-3 gap-10">
                    {apiArtifacts.sdks.map((sdk, index) => (
                        <SdkCard key={index} sdk={sdk} />
                    ))}
                    <SdkCardLayout
                        icon={<PythonLogo className="fill-neutral-400" />}
                        title={<div className="text-neutral-400">Python</div>}
                        rightElement={
                            <div className="rounded-full bg-neutral-500/20 px-3 py-1 font-medium uppercase text-neutral-400">
                                Coming Soon
                            </div>
                        }
                    />
                    <SdkCardLayout
                        icon={<JavaLogo className="fill-neutral-400" />}
                        title={<div className="text-neutral-400">Java</div>}
                        rightElement={
                            <div className="rounded-full bg-neutral-500/20 px-3 py-1 font-medium uppercase text-neutral-400">
                                Coming Soon
                            </div>
                        }
                    />
                    <SdkCardLayout
                        icon={<GoLogo className="fill-neutral-400" />}
                        title={<div className="text-neutral-400">Go</div>}
                        rightElement={
                            <div className="rounded-full bg-neutral-500/20 px-3 py-1 font-medium uppercase text-neutral-400">
                                Coming Soon
                            </div>
                        }
                    />
                    <SdkCardLayout
                        icon={<RubyLogo className="fill-neutral-400" />}
                        title={<div className="text-neutral-400">Ruby</div>}
                        rightElement={
                            <div className="rounded-full bg-neutral-500/20 px-3 py-1 font-medium uppercase text-neutral-400">
                                Coming Soon
                            </div>
                        }
                    />
                    <SdkCardLayout
                        icon={<DotNetLogo className="fill-neutral-400" />}
                        title={<div className="text-neutral-400">.NET</div>}
                        rightElement={
                            <div className="rounded-full bg-neutral-500/20 px-3 py-1 font-medium uppercase text-neutral-400">
                                Coming Soon
                            </div>
                        }
                    />
                </div>
            </div>
        </PageMargins>
    );
};